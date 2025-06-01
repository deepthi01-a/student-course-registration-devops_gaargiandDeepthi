import React from 'react';
import CourseCard from './CourseCard';

export default function CourseList({ courses, onRegister }) {
  if (!courses.length) return <p>No courses available.</p>;

  return (
    <div>
      {courses.map((course) => (
        <CourseCard key={course.id} course={course} onRegister={onRegister} />
      ))}
    </div>
  );
}
