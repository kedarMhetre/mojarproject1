import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from fpdf import FPDF
except ImportError:
    install("fpdf")
    from fpdf import FPDF

qa_list = [
    ("1. What is the primary role of Web Development?", "Web development involves building and maintaining websites and web applications to provide seamless functionality and good user experiences."),
    ("2. What does frontend development focus on?", "Frontend development focuses on the user interface (UI) and user experience (UX) using HTML, CSS, and JavaScript. It deals with what the user interacts with directly."),
    ("3. What is the responsibility of backend development?", "Backend development manages the server, database, and application logic. It processes data and ensures the frontend has the information it needs."),
    ("4. Which programming languages are commonly used for frontend?", "HTML (for structure), CSS (for styling), and JavaScript (for interactivity)."),
    ("5. Name some common backend programming languages.", "Python, PHP, Node.js (JavaScript), Java, Ruby, and C# are commonly used for backend logic."),
    ("6. What is the purpose of HTML?", "HTML (HyperText Markup Language) provides the fundamental structure and content of a web page."),
    ("7. What is the purpose of CSS?", "CSS (Cascading Style Sheets) is used for styling the visual layout of a website, including colors, fonts, spacing, and responsive design."),
    ("8. Why is JavaScript important in web development?", "JavaScript adds dynamic behavior and interactivity to web pages, such as animations, form validations, and asynchronous content updates."),
    ("9. What are web frameworks and libraries?", "They are pre-written code structures (like React, Angular, Django, Laravel) that help developers build web applications faster and more securely."),
    ("10. What is responsive web design?", "Responsive design ensures that a website looks and functions well across all device types and screen sizes, especially mobile devices."),
    ("11. How do you ensure mobile responsiveness?", "By using CSS media queries, flexible grid layouts, and fluid images to adapt the layout based on the screen width."),
    ("12. What is website performance optimization?", "It involves techniques like minimizing file sizes, using caching, and optimizing images to ensure a website loads quickly and runs smoothly."),
    ("13. Why is website speed important?", "Fast-loading websites improve user experience, reduce bounce rates, and rank higher in search engine results (SEO)."),
    ("14. What is web debugging?", "Debugging is the process of identifying, tracing, and fixing bugs or errors in the application's code to ensure expected functionality."),
    ("15. What role does testing play in web development?", "Testing ensures the web application works correctly under various conditions. It includes unit testing, integration testing, and user acceptance testing."),
    ("16. Why is security important in web development?", "Security protects user data, prevents malicious attacks (like hacking or data breaches), and builds trust with users."),
    ("17. What is SQL Injection?", "It is a security vulnerability where an attacker interferes with the database queries, potentially gaining unauthorized access to data."),
    ("18. How can you prevent Cross-Site Scripting (XSS)?", "By properly sanitizing and validating all user inputs and escaping outputs before rendering them in the browser."),
    ("19. What is a database?", "A database is a structured collection of data. Backend systems use databases (like MySQL, PostgreSQL, MongoDB) to store and retrieve user information."),
    ("20. How do designers and developers collaborate?", "Designers create the visual layout and user experience, while developers write the code to implement those designs, ensuring visual alignment with functionality."),
    ("21. What is an API?", "An API (Application Programming Interface) allows different software applications to communicate with each other, often used to connect the frontend to the backend."),
    ("22. Explain the difference between GET and POST HTTP methods.", "GET is used to retrieve data from a server, while POST is used to send data to the server (e.g., submitting a form)."),
    ("23. What is version control, and why use it?", "Version control systems (like Git) track changes to code over time, allowing multiple developers to collaborate and revert to previous versions if needed."),
    ("24. What is DOM (Document Object Model)?", "The DOM is a programming interface for HTML. It represents the page so that programs (like JavaScript) can change the document structure, style, and content."),
    ("25. What is semantic HTML?", "Semantic HTML uses tags that convey the meaning of the content (like <header>, <article>, <footer>) instead of just defining presentation, aiding accessibility and SEO."),
    ("26. What is the CSS Box Model?", "It is a box that wraps around every HTML element, consisting of margins, borders, padding, and the actual content."),
    ("27. Explain Closures in JavaScript.", "A closure is a feature in JavaScript where an inner function has access to the outer function's variables, even after the outer function has finished executing."),
    ("28. What are Promises in JavaScript?", "Promises represent the eventual completion (or failure) of an asynchronous operation and its resulting value, avoiding 'callback hell'."),
    ("29. How is Python used in web development?", "Python is used extensively in backend development with frameworks like Django and Flask to build robust, scalable server-side logic and APIs."),
    ("30. What are the benefits of using PHP?", "PHP is a popular server-side scripting language designed specifically for web development, deeply integrated with databases like MySQL and widely used in platforms like WordPress."),
    ("31. What is MVC architecture?", "Model-View-Controller (MVC) is a software design pattern that separates application logic into three interconnected components, promoting organized and modular code."),
    ("32. What is asynchronous programming?", "It allows programs to perform tasks like fetching data without freezing the main execution thread, improving responsiveness."),
    ("33. What is CORS?", "Cross-Origin Resource Sharing (CORS) is a security feature that restricts or allows web applications running at one origin to interact with resources from a different origin."),
    ("34. Explain the concept of Web Servers.", "A web server (like Apache or Nginx) stores, processes, and delivers web pages to users upon request via HTTP."),
    ("35. What is a Content Delivery Network (CDN)?", "A CDN is a geographically distributed network of servers that caches content closer to users, improving website loading speeds globally."),
    ("36. What is caching?", "Caching stores a copy of resources (like images or entire web pages) temporarily so future requests for that data can be served faster."),
    ("37. What is HTTPS?", "HTTPS is the secure version of HTTP, utilizing encryption (SSL/TLS) to protect data transmitted between the user's browser and the web server."),
    ("38. What is the difference between inline, inline-block, and block elements?", "Block elements take up the full width, inline elements only take up as much width as necessary (and ignore top/bottom margins), and inline-block behaves like inline but allows setting width and height."),
    ("39. Explain Event Delegation in JavaScript.", "Event delegation involves attaching a single event listener to a parent element to manage events for its children, improving performance and simplifying code."),
    ("40. What is an ORM (Object-Relational Mapping)?", "ORM is a programming technique used in frameworks (like Django ORM) to convert data between incompatible type systems using object-oriented programming, simplifying database queries."),
    ("41. How do sessions work in web applications?", "Sessions store user data across multiple requests (like being logged in). The server gives the client a session ID stored in a cookie to track them."),
    ("42. What is Minification?", "Minification is the process of removing unnecessary characters (like whitespace and comments) from source code to reduce file size and improve load times."),
    ("43. What is Lazy Loading?", "Lazy loading is an optimization technique where resources (like images) are only loaded when they enter the user's viewport, saving bandwidth and speeding up initial load."),
    ("44. What is a RESTful API?", "It is an architectural style for APIs that uses standard HTTP methods and stateless communication to access and manipulate data as resources."),
    ("45. How does 'Let', 'Var', and 'Const' differ in JS?", "'Var' is function-scoped, while 'let' and 'const' are block-scoped. 'Const' cannot be reassigned after declaration, whereas 'let' and 'var' can."),
    ("46. What is Cross-Site Request Forgery (CSRF)?", "CSRF is an attack that tricks a logged-in user into executing unwanted actions on a web application where they are currently authenticated."),
    ("47. How do you align a website's visuals with its functionality?", "By maintaining constant communication between designers and developers, conducting UI/UX reviews, and ensuring the technical implementation accurately reflects the design prototypes."),
    ("48. Why is having an online presence essential for businesses?", "It increases visibility, builds credibility, provides a platform to engage with customers globally, and serves as a powerful marketing and sales tool."),
    ("49. What is a Full-Stack Developer?", "A full-stack developer is proficient in both frontend and backend development, capable of building a complete web application from start to finish."),
    ("50. How do you keep up with web development trends?", "By following industry blogs, participating in developer communities (like GitHub or StackOverflow), attending conferences, and continuously learning new tools and frameworks.")
]

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "50 Web Development Interview Questions & Answers", ln=True, align='C')
pdf.ln(10)

# Questions
for q, a in qa_list:
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(0, 8, q)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, a)
    pdf.ln(5)

output_path = r"c:\mojarproject1\Web_Development_Interview_Questions.pdf"
pdf.output(output_path)
print(f"PDF generated successfully at {output_path}")
