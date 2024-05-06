# WebsiteCreation

Welcome to WebsiteCreation, a personalized website creation software designed specifically for colleges and universities.

## Overview

WebsiteCreation simplifies the process of creating individualized websites for students based on a hierarchical folder structure. Follow these easy steps to get started:

1. **Enter College Name:** Provide the name of the college (e.g., SMVITM).
  
2. **Upload Template HTML:** Submit the `StudentWebsite.html` file, containing the standard webpage for students.
  
3. **Upload Student Data:** Utilize the `StudentWebsite.xlsx` or `StudentWebsite.csv` file, including student information in the format:
| Year of Admission | Branch | USN         | Name       | Email         | Mobile Number | Image Link                                                                                                                     |
|-------------------|--------|-------------|------------|---------------|---------------|--------------------------------------------------------------------------------------------------------------------------------|
| 2021              | CS     | 4MW21CS001  | Nishita    | a@gmail.com   | #NAME?        | ![Image](https://th.bing.com/th/id/OIG2.jR6rWgNLrCpjuiK4fNh9?w=270&h=270&c=6&r=0&o=5&pid=ImgGn)                            |
| 2021              | CS     | 4MW21CS002  | Yukta      | b@gmail.com   | #NAME?        | ![Image](https://th.bing.com/th/id/OIG2.jR6rWgNLrCpjuiK4fNh9?w=270&h=270&c=6&r=0&o=5&pid=ImgGn)                            |
| 2021              | CS     | 4MW21CS003  | Navya      | c@gmail.com   | #NAME?        | ![Image](https://th.bing.com/th/id/OIG2.jR6rWgNLrCpjuiK4fNh9?w=270&h=270&c=6&r=0&o=5&pid=ImgGn)                            |
| 2021              | CS     | 4MW21CS004  | Katyayini  | d@gmail.com   | #NAME?        | ![Image](https://th.bing.com/th/id/OIG2.jR6rWgNLrCpjuiK4fNh9?w=270&h=270&c=6&r=0&o=5&pid=ImgGn)                            |
| 2021              | CS     | 4MW21CS005  | Krishna    | e@gmail.com   | #NAME?        | ![Image](https://th.bing.com/th/id/OIG2.jR6rWgNLrCpjuiK4fNh9?w=270&h=270&c=6&r=0&o=5&pid=ImgGn)                            |
| 2021              | EC     | 4MW21EC001  | Dhanush    | a@gmail.com   | #NAME?        | ![Image](https://th.bing.com/th/id/OIG2.jR6rWgNLrCpjuiK4fNh9?w=270&h=270&c=6&r=0&o=5&pid=ImgGn)                            |
| 2021              | EC     | 4MW21EC002  | Shreya     | b@gmail.com   | #NAME?        | ![Image](https://th.bing.com/th/id/OIG2.jR6rWgNLrCpjuiK4fNh9?w=270&h=270&c=6&r=0&o=5&pid=ImgGn)                            |
| 2021              | EC     | 4MW21EC003  | Sharan     | c@gmail.com   | #NAME?        | ![Image](https://th.bing.com/th/id/OIG2.jR6rWgNLrCpjuiK4fNh9?w=270&h=270&c=6&r=0&o=5&pid=ImgGn)                            |


The software will generate a structured folder for each student, creating HTML pages like:

- `SMVITM-20-CS-Krishna-Krishna.html`
- `SMVITM-20-CS-Ramesh-Ramesh.html`
- `SMVITM-20-CS-Dhanush-Dhanush.html`

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ramachandra-2k96/CreateWebsite
    ```

2. **Run the software:**

    ```bash
    nohup python3 manage.py runserver 0.0.0.0:2000 > output_file_website.txt 2>&1 &
    ```

## Features

- **Modern Interface:** User-friendly design for a seamless experience.
  
- **Multi-Language Support:** Choose from English, Spanish, or German for diverse user preferences.
  
- **Enhanced HTML Page Generation:** Improved function to create HTML pages based on student data.
  
- **File Naming Style:** Updated zip file naming with the timestamp for better organization.
  
- **Multiple filetype support:** User can input his data in csv or xlsx formate

## Feedback

Your feedback is crucial to us! If you have any comments, suggestions, or encounter issues, please reach out to us at [ramachandraudupa2004@gmail.com](mailto:ramachandraudupa2004@gmail.com) or [ramachandra.21ad043@sode-edu.in](mailto:ramachandra.21ad043@sode-edu.in).

## Example

For a quick example, check the [Python code](https://github.com/Ramachandra-2k96/Python/tree/b74e7643e7b07392cac47add9188f151ecc828d3/Personalised%20website).

Thank you for choosing WebsiteCreation! Happy coding!
