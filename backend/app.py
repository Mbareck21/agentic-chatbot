from flask import Flask, request, jsonify
from flask_cors import CORS
import re
from smolagents.agents import ToolCallingAgent
from smolagents import tool, LiteLLMModel
from smolagents import DuckDuckGoSearchTool
from smolagents import CodeAgent

app = Flask(__name__)
CORS(app)

def clean_agent_response(response: str) -> str:
    patterns = [
        r"Thought:.*?(?=\n|$)",
        r"Code:.*?```.*?```",
        r"print\(.*?\)",
        r"\[Step \d+:.*?\]",
        r"Out: .*?(?=\n|$)",
        r"<end_code>",
        r"\n\s*\n",
        r"```tool_code.*?```",
        r"Based on the search results,",
        r"I will bypass.*?directly\.",
        r"I will use another web search.*?$",
        r"The agent is struggling.*?$"
    ]
    
    cleaned = response
    for pattern in patterns:
        cleaned = re.sub(pattern, "", cleaned, flags=re.DOTALL)
    cleaned = " ".join(cleaned.split())
    return cleaned

model = LiteLLMModel(model_id="gemini/gemini-2.0-flash-exp")
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400
    
    response = agent.run(user_message)
    cleaned_response = clean_agent_response(response)
    return jsonify({'response': cleaned_response})

if __name__ == '__main__':
    app.run(port=5000)