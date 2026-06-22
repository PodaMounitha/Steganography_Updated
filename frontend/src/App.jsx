import { useState } from 'react';
import './App.css';
import HideFile from './components/HideFile';
import ExtractFile from './components/ExtractFile';

function App() {
  const [activeTab, setActiveTab] = useState('hide');

  return (
    <div className="app-container">
      <div className="header">
        <h1>StealthVault</h1>
        <p>Secure File Steganography</p>
      </div>

      <div className="main-card glass-panel">
        <div className="tabs">
          <button 
            className={`tab-btn ${activeTab === 'hide' ? 'active' : ''}`}
            onClick={() => setActiveTab('hide')}
          >
            Hide File
          </button>
          <button 
            className={`tab-btn ${activeTab === 'extract' ? 'active' : ''}`}
            onClick={() => setActiveTab('extract')}
          >
            Extract File
          </button>
        </div>

        <div className="tab-content">
          {activeTab === 'hide' ? <HideFile /> : <ExtractFile />}
        </div>
      </div>
    </div>
  );
}

export default App;
