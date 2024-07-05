

__If you have vs code, Use the keyboard shortcut Ctrl+Shift+V (Windows/Linux) or Cmd+Shift+V (Mac) to open the preview pane (to view this README file in a readable format)__

# Backend (navigate to the backend directory)
> make sure you are in the backend directory
1. Create a python virtual env; And install dependencies
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
2. First-time setup [may need if data is not available]
```bash
python manage.py makemigrations
python manage.py migrate
```
3. Start the backend server
```bash
python manage.py runserver
```

# Frontend (navigate to the frontend directory)
> make sure you are in the frontend directory
### Make sure you have node and vue is installed in your system
1. Install dependencies
```bash
npm i
```
2. If you face any issues in the above step, Install deependencies using UI
```bash
vue ui
```
3. VUE Project Manager will be opened in the browser, add current directory.
+ Check for plugins and Dependencies in the side panel, select and install them

4. Once dependecies installed, then follow the below steps

5. Start the frontend server
```bash
npm run serve
```
6. Open the url in browser
http://localhost:8080/ 



# App walk through

> Registration Screen

- Registration Form
![Registration Form](<snaps/Screenshot (55).png>)

- Re-registering with already registered username
![Re-registering with already registered username](<snaps/Screenshot (56).png>)

> Login Screen
- Login Form (wrong credentials)
![Login Form](<snaps/Screenshot (54).png>)

> Login successful > Home Screen

![Login successful; Redirected to Home Screen](<snaps/Screenshot (59).png>)

> Employees Screen
- search keyword has been highlited
![Employees Screen; search keyword has been highlited](<snaps/Screenshot (61).png>)
- Additional Filter form
![Filter Form](<snaps/Screenshot (62).png>)
- Filter keywords also highlighted
![Filter keywords also highlighted](<snaps/Screenshot (63).png>)

> Leads Screen
![Leads screen](<snaps/Screenshot (64).png>)

> API Docs Screen
![API Documentation](<snaps/Screenshot (65).png>)
