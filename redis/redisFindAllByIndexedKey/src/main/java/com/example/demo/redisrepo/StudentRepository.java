package com.example.demo.redisrepo;

import com.example.demo.entity.Student;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface StudentRepository extends CrudRepository<Student, String> {
    List<Student> findByName(String name);

    List<Student> findByNameAndGrade(String name, String grade);

}