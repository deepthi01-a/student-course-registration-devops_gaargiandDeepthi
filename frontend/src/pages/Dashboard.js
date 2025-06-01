import React, { useEffect, useState, useContext } from 'react';
import api from '../services/api';
import AuthContext from '../auth';
import CourseList from '../components/CourseList';

export default function Dashboard() {
  const { user } = useContext(AuthContext);
  const [courses, setCourses] = useState([]);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  useEffect(() => {
    async function fetchCourses() {
      try {
        const res = await api.get('/student/courses');
        setCourses(res.data.courses);
      } catch (err) {
        setError('Failed to load courses');
      }
    }
    fetchCourses();
  }, []);

  const handleRegister = async (courseId) => {
    setError('');
    setSuccess('');
    try {
      await api.post('/student/register_course', { course_id: courseId });
      setSuccess('Successfully registered for the course!');
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed');
    }
  };

  if (!user) {
    return <p>Please login to see your dashboard.</p>;
  }

  return (
    <div>
      <h2>Welcome, {user.name}!</h2>
      {error && <p style={{color: 'red'}}>{error}</p>}
      {success && <p style={{color: 'green'}}>{success}</p>}
      <h3>Available Courses</h3>
      <CourseList courses={courses} onRegister={handleRegister} />
    </div>
  );
}
