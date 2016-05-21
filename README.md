# RealTimeImageProcessor
a tiny python class that allows you to quickly apply your own process function to video camera using opencv function
# Example

```
rip = RealTimeImageProcessor(1)
rip.set_process_function(lambda x: cv2.cvtColor(x,cv2.COLOR_BGR2GRAY))
rip.run("test")
```

