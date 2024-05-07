package com.tech.eureka.rest;

import com.netflix.discovery.EurekaClient;
import com.tech.eureka.restinterface.GreetingController;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Lazy;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RestClientEureka implements GreetingController {

    @Value("${spring.application.name}")
    private String appName;

    @Autowired
    @Lazy
    private EurekaClient eurekaClient;

    @Override
    public String greeting() {
        return String.format(
                "Hello from '%s'!", eurekaClient.getApplication(appName).getName());
    }
}
