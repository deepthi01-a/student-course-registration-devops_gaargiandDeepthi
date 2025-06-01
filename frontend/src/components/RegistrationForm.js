import React from 'react';

export default function RegistrationForm({ courseId, onSubmit }) {
  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(courseId);
  };

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Register for Course</button>
    </form>
  );
}
