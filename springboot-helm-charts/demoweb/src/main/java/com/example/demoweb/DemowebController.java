package devops.cstu.org.demo

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/")
public class DemowebController {

    @GetMapping("/")
    public String home() {
        return "Hello World.";
    }
}
