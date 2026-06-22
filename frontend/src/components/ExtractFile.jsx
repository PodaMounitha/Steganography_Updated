import { useState } from 'react';
import FileUpload from './FileUpload';
import { extractFile } from '../services/api';

const ExtractFile = () => {
  const [image, setImage] = useState(null);
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image || !password) {
      setError('Please provide the stego image and password.');
      return;
    }

    setLoading(true);
    setError('');
    setSuccess(false);

    try {
      const blob = await extractFile(image, password);
      
      // Try to determine the filename from the blob headers if possible, 
      // but since axios might not expose Content-Disposition easily without extra config,
      // we'll use a generic name or prompt the user.
      const url = window.URL.createObjectURL(new Blob([blob]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'extracted_secret_file'); // Fallback name
      document.body.appendChild(link);
      link.click();
      
      // Cleanup
      link.parentNode.removeChild(link);
      window.URL.revokeObjectURL(url);
      
      setSuccess(true);
    } catch (err) {
      console.error(err);
      setError('Failed to extract file. Incorrect password or image is not a valid stego image.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="animate-fade-in">
      <form onSubmit={handleSubmit}>
        <FileUpload 
          label="Stego Image" 
          accept="image/*" 
          onChange={setImage} 
        />
        
        <div className="form-group">
          <label>Password (Decryption Key)</label>
          <input 
            type="password" 
            placeholder="Enter the password used during hiding" 
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        {error && <div style={{ color: '#ef4444', marginBottom: '1rem' }}>{error}</div>}
        {success && <div style={{ color: '#10b981', marginBottom: '1rem' }}>File extracted successfully! Download should begin shortly.</div>}

        <button 
          type="submit" 
          className="btn-primary" 
          disabled={loading || !image || !password}
        >
          {loading ? <span className="spinner"></span> : 'Extract File'}
        </button>
      </form>
    </div>
  );
};

export default ExtractFile;
