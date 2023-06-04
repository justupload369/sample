package com.example.demo.rest;

import com.example.demo.entity.Student;
import com.example.demo.entity.TestPojo;
import com.example.demo.redisrepo.StudentRepository;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Test {
    @Autowired
    private StudentRepository studentRepository;

    @Autowired
    private ObjectMapper objectMapper;

    @PostMapping(value = "/insert", produces = MediaType.APPLICATION_JSON_VALUE)
    public String insert(@RequestBody TestPojo testPojo) {
        Student student = new Student();
        student.setId(testPojo.getId());
        student.setName(testPojo.getName());
        student.setGrade(testPojo.getGrade());
        studentRepository.save(student);
        return "Student inserted into redis";
    }

    @PostMapping(value = "/getallstudents", produces = MediaType.APPLICATION_JSON_VALUE)
    public String findAllStudents(@RequestBody TestPojo testPojo) throws JsonProcessingException {
        return objectMapper.writeValueAsString(studentRepository.findAll());
    }

    @PostMapping(value = "/findbyid", produces = MediaType.APPLICATION_JSON_VALUE)
    public String findById(@RequestBody TestPojo testPojo) throws JsonProcessingException {
        return objectMapper.writeValueAsString(studentRepository.findById(testPojo.getId()));
    }

    @PostMapping(value = "/findbyname", produces = MediaType.APPLICATION_JSON_VALUE)
    public String findByName(@RequestBody TestPojo testPojo) throws JsonProcessingException {
        return objectMapper.writeValueAsString(studentRepository.findByName(testPojo.getName()));
    }

    @PostMapping(value = "/findbynameandgrade", produces = MediaType.APPLICATION_JSON_VALUE)
    public String findByNameAndGrade(@RequestBody TestPojo testPojo) throws JsonProcessingException {
        return objectMapper.writeValueAsString(studentRepository.findByNameAndGrade(testPojo.getName(), testPojo.getGrade()));
    }


}
