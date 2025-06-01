-- sample_data.sql

-- Insert sample users
INSERT INTO users (name, email, password_hash, is_admin) VALUES
('Admin User', 'admin@example.com', '$2b$12$CwTycUXWue0Thq9StjUM0uJ8zv1ePFSv3ch0e6iyr.E0.07VlYZ8W', TRUE), -- password: admin123
('Student One', 'student1@example.com', '$2b$12$U7q8FojXxSJ3.rkpqD7y1uyAzCjgDqmt57Kk1fJhlGv0QwoHnCFzy', FALSE); -- password: student123

-- Insert sample courses
INSERT INTO courses (name, description) VALUES
('Introduction to Programming', 'Learn basics of programming using Python.'),
('Web Development', 'Build web apps using HTML, CSS, JavaScript, and React.'),
('Data Structures', 'Understand core data structures and algorithms.');

-- Sample registrations (optional)
INSERT INTO registrations (user_id, course_id) VALUES
(2, 1);
