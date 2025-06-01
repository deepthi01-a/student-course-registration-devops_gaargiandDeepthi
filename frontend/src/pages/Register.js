import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';

export default function Register() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isAdmin, setIsAdmin] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    try {
      await api.post('/auth/register', { name, email, password, is_admin: isAdmin });
      setSuccess('Registration successful! You can now login.');
      setTimeout(() => navigate('/login'), 2000);
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed');
    }
  };

  return (
    <div>
      <h2>Register</h2>
      {error && <p style={{color: 'red'}}>{error}</p>}
      {success && <p style={{color: 'green'}}>{success}</p>}
      <form onSubmit={handleSubmit}>
        <label>Name:</label><br />
        <input type="text" value={name} onChange={e => setName(e.target.value)} required /><br />
        <label>Email:</label><br />
        <input type="email" value={email} onChange={e => setEmail(e.target.value)} required /><br />
        <label>Password:</label><br />
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} required /><br />
        <label>
          <input type="checkbox" checked={isAdmin} onChange={e => setIsAdmin(e.target.checked)} />
          Register as Admin
        </label><br />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}
