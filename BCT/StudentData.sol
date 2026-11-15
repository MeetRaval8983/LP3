
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    // Structure to store student information
    struct Student {
        uint256 rollNo;
        string name;
        uint256 marks;
    }

    // Array to store multiple students
    Student[] public students;

    // Add student data
    function addStudent(
        uint256 _rollNo,
        string memory _name,
        uint256 _marks
    ) public {
        students.push(Student(_rollNo, _name, _marks));
    }

    // Get total number of students
    function getStudentCount() public view returns (uint256) {
        return students.length;
    }

    // Get student details by array index
    function getStudent(uint256 index)
        public
        view
        returns (uint256, string memory, uint256)
    {
        require(index < students.length, "Invalid student index");

        Student memory s = students[index];
        return (s.rollNo, s.name, s.marks);
    }

    // Fallback function executes for unmatched calls
    // or calls with calldata that do not match a function
    fallback() external payable {
    }

    // Accept plain ETH transfers
    receive() external payable {
    }
}
