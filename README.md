# AI Chat Agent

A modern chat interface powered by a Next.js frontend and Flask backend with AI capabilities.

## Features
- Real-time chat interface
- AI-powered responses using Gemini model
- Modern UI with shadcn/ui components
- Web search capabilities
- Clean message formatting

## Technologies
### Frontend
- Next.js 14
- TypeScript
- shadcn/ui components
- TailwindCSS
- React Query for data fetching

### Backend
- Flask
- Python
- smolagents for AI integration
- Flask-CORS for cross-origin support
- Gemini AI model

## Project Structure
. ├── frontend/ │ ├── app/ │ │ ├── page.tsx # Main chat interface │ │ ├── layout.tsx # Root layout │ │ └── globals.css # Global styles │ ├── components/ # UI components │ └── lib/ # Utilities └── backend/ ├── app.py # Flask server └── requirements.txt # Python dependencies

## Setup

### Prerequisites
- Node.js 18+
- Python 3.8+
- npm or yarn
- pip

### Frontend Setup
```bash
cd frontend
npm install
npm run dev

Backend will run on http://localhost:5000

### Development
Start the backend server
Start the frontend development server
Make changes to the code
Frontend hot-reloads automatically
Backend requires manual restart
Contributing
Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Create a Pull Request
License
MIT License# agentic-chatbot
