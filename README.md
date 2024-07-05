

__If you have vs code, Use the keyboard shortcut Ctrl+Shift+V (Windows/Linux) or Cmd+Shift+V (Mac) to open the preview pane (to view this README file in a readable format)__

# Backend (navigate to the backend directory)
> make sure you are in the backend directory
1. Activate virtual environment 
```bash
.\venv\Scripts\activate
```
2. Start the backend server
```bash
python manage.py runserver
```
> If you face any issues, then follow the below steps for backend
2. If above steps not working or facing any issues, create a new virtual env if not working; And install dependencies
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
3. First-time setup [may need if data is not available]
```bash
python manage.py makemigrations
python manage.py migrate
```

# Frontend (navigate to the frontend directory)
> make sure you are in the frontend directory
### Make sure you have node and vue is installed in your system
1. Start the frontend server
```bash
npm run serve
```
2. Open the url in browser
http://localhost:8080/ 

> If you face any issues, then follow below steps
3. Install dependencies
```bash
npm i
```
4. If you face any issues in the above step, Install deependencies using UI
```bash
vue ui
```
5. App UI will be opened in the browser, you can select plugins and dependencies to manually install them

6. Once dependecies installed, then follow the steps 1 and 2 to start the frontend server


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
