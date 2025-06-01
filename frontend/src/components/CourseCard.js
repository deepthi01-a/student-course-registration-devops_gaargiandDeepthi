import React from 'react';

export default function CourseCard({ course, onRegister }) {
  return (
    <div style={{ border: '1px solid #ccc', marginBottom: '8px', padding: '10px' }}>
      <h3>{course.name}</h3>
      <p>{course.description}</p>
      <button onClick={() => onRegister(course.id)}>Register</button>
    </div>
  );
}
