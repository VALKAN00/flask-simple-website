USE cloud_project;

-- Table structure for table `students`
CREATE TABLE IF NOT EXISTS `students` (
  `std_id` int NOT NULL,
  `std_name` varchar(50) NOT NULL,
  `std_age` float NOT NULL,
  `std_cgpa` float NOT NULL,
  `std_department` varchar(50) NOT NULL,
  `std_phone` int DEFAULT NULL,
  `std_email` varchar(50) DEFAULT NULL,
  `std_address` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`std_id`)
);

-- Insert sample data into `students`
INSERT INTO `students` VALUES
(22010027,'Ahmed Emad Abdelfattah',19,3.94,'data science',77788,'ahmed@example.com','789 Oak Ave'),
(22010100,'Ziad Mohammed Elkhateeb',19,3.94,'data science',12345,'ziad@example.com','123 Main St'),
(22010231,'Mohammed Mahmoud Naeem',19,3.945,'data science',98765,'mohamed@example.com','321 Pine St'),
(22011438,'Qamar Mosallam Barazi',19,3.95,'data science',55512,'qamar@example.com','123 Main St'),
(22011620,'Abdelrhman Ahmed Mohamed',21,3.935,'data science',98765,'abdelrhman@example.com','456 Elm St');