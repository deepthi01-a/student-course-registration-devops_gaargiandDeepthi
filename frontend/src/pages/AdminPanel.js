import React, { useState, useContext } from 'react';
import api from '../services/api';
import AuthContext from '../auth';

export default function AdminPanel() {
  const { user } = useContext(AuthContext);
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  if (!user || !user.is_admin) {
    return <p>Access denied. Admins only.</p>;
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    try {
      await api.post('/admin/add_course', { name, description });
      setSuccess('Course added successfully!');
      setName('');
      setDescription('');
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to add course');
    }
  };

  return (
    <div>
      <h2>Admin Panel</h2>
      {error && <p style={{color: 'red'}}>{error}</p>}
      {success && <p style={{color: 'green'}}>{success}</p>}
      <form onSubmit={handleSubmit}>
        <label>Course Name:</label><br />
        <input value={name} onChange={e => setName(e.target.value)} required /><br />
        <label>Description:</label><br />
        <textarea value={description} onChange={e => setDescription(e.target.value)} required /><br />
        <button type="submit">Add Course</button>
      </form>
    </div>
  );
}
