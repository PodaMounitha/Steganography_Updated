import { useState } from 'react';
import './FileUpload.css';

const FileUpload = ({ label, accept, onChange }) => {
  const [dragActive, setDragActive] = useState(false);
  const [fileName, setFileName] = useState('');

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const handleChange = (e) => {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  };

  const handleFile = (file) => {
    setFileName(file.name);
    onChange(file);
  };

  return (
    <div className="form-group">
      <label>{label}</label>
      <div 
        className={`file-upload-container ${dragActive ? 'drag-active' : ''}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
      >
        <input 
          type="file" 
          className="file-upload-input" 
          accept={accept} 
          onChange={handleChange} 
        />
        <div className="file-upload-content">
          <svg className="upload-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z"/>
          </svg>
          {fileName ? (
            <span className="file-name">{fileName}</span>
          ) : (
            <>
              <span style={{ fontWeight: 600 }}>Click to upload or drag and drop</span>
              <span className="upload-hint">SVG, PNG, JPG or GIF (max. 800x400px)</span>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default FileUpload;
