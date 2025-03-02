# 0x19 Postmortem: Strace Debugging Issue on Web Server

![Strace Debugging](https://miro.medium.com/v2/resize:fit:640/format:webp/1*3k3lSwb-QP-x9h0w28OIuQ.jpeg)

## **Issue Summary**
This postmortem outlines an issue I faced while trying to debug the Apache2 web server using `strace`. Despite several attempts to configure and run `strace` on Apache2 processes, it was unable to trace system calls, leading to challenges in diagnosing server issues. The problem was detected at 5:30 PM (SAST), and as of now, it remains unresolved. Additional troubleshooting steps are outlined below.

### **Duration of the Outage**
- **Start Time**: 5:30 PM (SAST)
- **End Time**: Ongoing (issue unresolved as of the last update)
- **Impact**: The inability to use `strace` on Apache2 processes has severely hindered server-side diagnostics. This has impacted all users relying on the server, as proper debugging could not be performed. The issue prevents deeper analysis of server behavior.

### **Root Cause**
- The root cause was determined to be a **permissions issue** that prevented `strace` from attaching to Apache2 processes. Specifically, `strace` requires elevated privileges (root or `sudo`) to trace system calls for processes that are running under non-privileged users, such as Apache2.

---

## **Timeline**
- **5:30 PM (SAST)**: The issue was first detected when attempting to run `strace` on Apache2 processes. No useful output was generated.
- **5:35 PM (SAST)**: Initial investigation began, using commands like `grep apache2` and `curl -sl localhost` to check if the server was running. These commands showed that the server was functioning, but `strace` failed to produce any meaningful information.
- **5:50 PM (SAST)**: Checked the installation status of `strace` using `dpkg -s strace` to confirm that it was correctly installed.
- **6:00 PM (SAST)**: Assumed that `strace` might be missing the necessary permissions to attach to Apache2 processes. Began investigating Apache2’s running processes to identify any discrepancies.
- **6:30 PM (SAST)**: Realized that `strace` likely needed elevated privileges (using `sudo` or running as root) to trace Apache2, as it was running under a non-privileged user.
- **7:00 PM (SAST)**: Consulted official documentation and community discussions to better understand the specific permissions and configuration requirements for running `strace` with Apache2 processes.
- **7:30 PM (SAST)**: As of this writing, the issue remains unresolved. However, recommendations for fixing the issue have been identified, including the need for elevated permissions.

---

## **Root Cause and Resolution**

### **Cause**
The core issue stems from `strace`'s inability to access Apache2 processes due to improper permissions. Apache2, like many services, runs as a non-privileged user, and `strace` requires root or `sudo` access to attach to these processes. The lack of the necessary privileges for `strace` to interact with Apache2 was the primary cause of the issue.

### **Resolution**
While the issue remains ongoing, it can likely be resolved by modifying the permissions for `strace` or by running the tool with elevated privileges using `sudo`. Additionally, system security settings may need to be adjusted to allow `strace` to interact with Apache2 processes. Further investigation into user permissions and Apache2's configuration is required to resolve the issue completely.

---

## **Corrective and Preventative Measures**

### **Improvements Needed**
- Ensure that `strace` has the necessary permissions to trace Apache2 processes. This could involve adjusting system security policies or using elevated privileges for `strace`.
- Double-check the `strace` installation and configuration to ensure that it's properly set up to debug Apache2 processes.

### **To-Do List**
1. **Verify and adjust file permissions** related to `strace` and Apache2 processes to allow `strace` to function correctly.
2. **Ensure Apache2 is running under a user** that allows debugging with `strace` (consider adjusting user privileges if necessary).
3. **Test `strace` functionality** on a new, clean web server setup to confirm the issue is resolved and that permissions are set properly.
4. **Update configuration management** tools (e.g., Puppet) to ensure that `strace` is correctly configured and that permissions are set during server provisioning.

---
## System Monitoring Tools

Below is a diagram that provides an overview of Linux system performance monitoring and debugging tools, which can help in diagnosing similar issues in the future:
![System Monitoring Tools](https://miro.medium.com/v2/resize:fit:640/format:webp/1*V7gd1lQdjzJvfspaCHsUbw.png)

## **Conclusion**
The inability to debug Apache2 using `strace` has prevented effective troubleshooting, but it appears that the issue is related to permissions and configuration. Resolving this requires ensuring that `strace` has the necessary privileges to access Apache2 processes, which can be accomplished by running `strace` with elevated privileges or adjusting security settings. Further investigation is necessary, but the corrective actions outlined above should prevent similar issues in the future.
