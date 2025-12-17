import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!query.trim()) {
      setError('Please enter a query');
      return;
    }

    setLoading(true);
    setError('');
    setResponse('');

    try {
      const res = await axios.post('http://localhost:8000/query', {
        query: query
      });
      setResponse(res.data.response);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to get response. Make sure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <h1 className="title">Weather Query Assistant</h1>
        <p className="subtitle">Ask me about the weather in any city!</p>
        
        <form onSubmit={handleSubmit} className="query-form">
          <div className="input-group">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="e.g., What's the weather in Pune?"
              className="query-input"
              disabled={loading}
            />
            <button 
              type="submit" 
              className="send-button"
              disabled={loading}
            >
              {loading ? (
                <span className="loader"></span>
              ) : (
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <line x1="22" y1="2" x2="11" y2="13"></line>
                  <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                </svg>
              )}
            </button>
          </div>
        </form>

        {error && (
          <div className="message error-message">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="8" x2="12" y2="12"></line>
              <line x1="12" y1="16" x2="12.01" y2="16"></line>
            </svg>
            <p>{error}</p>
          </div>
        )}

        {response && (
          <div className="message response-message">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M3 18v-6a9 9 0 0 1 18 0v6"></path>
              <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path>
            </svg>
            <p>{response}</p>
          </div>
        )}

        <div className="examples">
          <p className="examples-title">Try asking:</p>
          <div className="example-buttons">
            <button onClick={() => setQuery("What's the weather in Pune?")} className="example-btn">
              Weather in Pune
            </button>
            <button onClick={() => setQuery("How's the weather in London today?")} className="example-btn">
              Weather in London
            </button>
            <button onClick={() => setQuery("Tell me the weather of Tokyo")} className="example-btn">
              Weather in Tokyo
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
