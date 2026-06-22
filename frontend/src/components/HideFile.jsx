import { useState } from 'react';
import FileUpload from './FileUpload';
import { hideFile, getDownloadUrl } from '../services/api';

const HideFile = () => {
  const [image, setImage] = useState(null);
  const [secretFile, setSecretFile] = useState(null);
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image || !secretFile || !password) {
      setError('Please provide all required fields.');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const data = await hideFile(image, secretFile, password);
      setResult(data);
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.error || 'An error occurred while hiding the file.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="animate-fade-in">
      <form onSubmit={handleSubmit}>
        <FileUpload 
          label="Cover Image" 
          accept="image/*" 
          onChange={setImage} 
        />
        
        <FileUpload 
          label="Secret File to Hide" 
          accept="*/*" 
          onChange={setSecretFile} 
        />
        
        <div className="form-group">
          <label>Password (Encryption Key)</label>
          <input 
            type="password" 
            placeholder="Enter a strong password" 
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        {error && <div style={{ color: '#ef4444', marginBottom: '1rem' }}>{error}</div>}

        <button 
          type="submit" 
          className="btn-primary" 
          disabled={loading || !image || !secretFile || !password}
        >
          {loading ? <span className="spinner"></span> : 'Hide File in Image'}
        </button>
      </form>

      {result && (
        <div className="result-container animate-fade-in">
          <h3>Successfully Hidden!</h3>
          
          <div className="metrics">
            <div className="metric-item">
              <div style={{ color: 'var(--text-secondary)' }}>MSE</div>
              <div className="metric-value">{parseFloat(result.mse).toFixed(2)}</div>
            </div>
            <div className="metric-item">
              <div style={{ color: 'var(--text-secondary)' }}>PSNR</div>
              <div className="metric-value">{parseFloat(result.psnr).toFixed(2)} dB</div>
            </div>
          </div>
          
          <div style={{ textAlign: 'center' }}>
            <img 
              src={getDownloadUrl(result.output_image)} 
              alt="Steganography Output Preview" 
              className="preview-image" 
            />
            <a 
              href={getDownloadUrl(result.output_image)} 
              download 
              target="_blank"
              rel="noreferrer"
              className="btn-primary" 
              style={{ display: 'inline-block', width: 'auto' }}
            >
              Download Secure Image
            </a>
          </div>
        </div>
      )}
    </div>
  );
};

export default HideFile;
