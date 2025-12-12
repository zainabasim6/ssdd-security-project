"""
🚨 INSECURE WEB APPLICATION - FOR SECURITY TESTING ONLY
This application contains multiple security vulnerabilities on purpose.
DO NOT deploy in production or expose to the internet!
"""

from flask import Flask, request, session, redirect, make_response
import sqlite3

app = Flask(__name__)
app.secret_key = 'insecure_secret_key'  # Hardcoded secret key

# Simple hardcoded users (🚨 VULNERABILITY: Plain text passwords)
users = {
    'admin': 'admin123',
    'user1': 'password123',
    'test': 'test'
}

# In-memory comments storage
comments = [
    "Welcome to the comment section!",
    "Remember: This app is for security testing only."
]

def render_html(title, content):
    """Helper function to render HTML pages"""
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{ font-family: Arial; padding: 20px; max-width: 800px; margin: 0 auto; }}
            .nav {{ background: #333; padding: 10px; margin-bottom: 20px; }}
            .nav a {{ color: white; margin-right: 15px; text-decoration: none; }}
            .alert {{ padding: 10px; margin: 10px 0; border-radius: 4px; }}
            .success {{ background: #d4edda; color: #155724; }}
            .error {{ background: #f8d7da; color: #721c24; }}
            .warning {{ background: #fff3cd; color: #856404; border-left: 4px solid #ffc107; padding: 10px; margin: 10px 0; }}
            form {{ margin: 20px 0; }}
            input, textarea {{ padding: 8px; margin: 5px 0; width: 300px; }}
            button {{ padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }}
            pre {{ background: #f5f5f5; padding: 15px; overflow: auto; }}
            code {{ background: #e9ecef; padding: 2px 4px; border-radius: 3px; }}
        </style>
    </head>
    <body>
        <div class="nav">
            <a href="/">Home</a>
            <a href="/login">Login</a>
            <a href="/search">Search</a>
            <a href="/comment">Comment</a>
            <a href="/debug">Debug</a>
            {f'<span style="color: lightgreen;">Logged in as: {session.get("user", "")}</span> <a href="/logout" style="color: #ff6b6b;">Logout</a>' if 'user' in session else ''}
        </div>
        
        <div class="warning">
            <strong>🚨 WARNING:</strong> This is an INSECURE application for security testing only!
        </div>
        
        {content}
    </body>
    </html>
    '''
    return html

# Routes
@app.route('/')
def home():
    content = '''
    <h1>🔓 Vulnerable Web Application</h1>
    <p>This application contains intentional security vulnerabilities for testing purposes.</p>
    
    <h2>Test These Vulnerabilities:</h2>
    <ul>
        <li><a href="/login">Login</a> - Weak authentication (no password hashing)</li>
        <li><a href="/search">Search</a> - SQL Injection vulnerability</li>
        <li><a href="/comment">Comment</a> - Cross-Site Scripting (XSS)</li>
        <li><a href="/debug">Debug</a> - Information leakage</li>
    </ul>
    
    <h2>Test Credentials:</h2>
    <pre>Username: admin | Password: admin123
Username: user1  | Password: password123</pre>
    
    <h2>Quick Test Payloads:</h2>
    <div class="warning">
        <strong>SQL Injection:</strong> <code>' OR '1'='1</code><br>
        <strong>XSS:</strong> <code>&lt;script&gt;alert('hacked')&lt;/script&gt;</code>
    </div>
    '''
    return render_html('Home - Vulnerable App', content)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        # 🚨 VULNERABILITY: No rate limiting, plain text comparison
        if username in users and users[username] == password:
            session['user'] = username
            content = f'''
            <h1>Login Successful!</h1>
            <p>Welcome, {username}!</p>
            <div class="success">✅ Logged in successfully</div>
            <p><a href="/">Go to Home</a></p>
            '''
            return render_html('Login Success', content)
        else:
            content = f'''
            <h1>Login</h1>
            <div class="error">❌ Invalid username or password</div>
            <form method="POST">
                <div>Username: <input type="text" name="username" value="{username}"></div>
                <div>Password: <input type="password" name="password"></div>
                <button type="submit">Login</button>
            </form>
            '''
            return render_html('Login Failed', content)
    
    # GET request - show login form
    content = '''
    <h1>Login</h1>
    <p>🚨 Vulnerabilities: Plain text passwords, no rate limiting</p>
    <form method="POST">
        <div>Username: <input type="text" name="username"></div>
        <div>Password: <input type="password" name="password"></div>
        <button type="submit">Login</button>
    </form>
    '''
    return render_html('Login', content)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # 🚨 CRITICAL VULNERABILITY: SQL Injection
    conn = sqlite3.connect(':memory:')  # Using in-memory database
    cursor = conn.cursor()
    
    # Create a simple table
    cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER, name TEXT, price REAL)')
    cursor.execute('DELETE FROM products')
    cursor.executemany('INSERT INTO products VALUES (?, ?, ?)', [
        (1, 'Laptop', 999.99),
        (2, 'Phone', 699.99),
        (3, 'Tablet', 499.99),
        (4, 'Headphones', 199.99)
    ])
    conn.commit()
    
    results = []
    if query:
        try:
            # 🚨 DANGER: Direct string concatenation - SQL INJECTION HERE!
            sql = f"SELECT * FROM products WHERE name LIKE '%{query}%'"
            cursor.execute(sql)
            results = cursor.fetchall()
        except Exception as e:
            results = [f"SQL Error: {str(e)}"]
    
    conn.close()
    
    # Build results display
    results_display = ""
    if query:
        results_display = f'<h3>Results for "{query}":</h3><pre>{results}</pre>'
    
    content = f'''
    <h1>Search Products</h1>
    <p>🚨 CRITICAL: SQL Injection vulnerability active!</p>
    
    <form method="GET" action="/search">
        <input type="text" name="q" value="{query}" placeholder="Search for products...">
        <button type="submit">Search</button>
    </form>
    
    <h3>Try these SQL Injection payloads:</h3>
    <div class="warning">
        <code>' OR '1'='1</code> - Show all products<br>
        <code>' UNION SELECT name, sql, null FROM sqlite_master--</code> - Get database schema<br>
        <code>'; DELETE FROM products--</code> - Delete data (test only!)
    </div>
    
    {results_display}
    '''
    
    return render_html('Search - SQL Injection Test', content)

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    global comments
    
    if request.method == 'POST':
        new_comment = request.form.get('comment', '')
        if new_comment:
            # 🚨 VULNERABILITY: Storing raw HTML (XSS)
            comments.append(new_comment)
    
    # Display comments (🚨 VULNERABILITY: No HTML escaping!)
    comments_html = ""
    for comment_text in comments:
        comments_html += f"<li>{comment_text}</li>"
    
    content = f'''
    <h1>Comment Section</h1>
    <p>🚨 Vulnerability: Cross-Site Scripting (XSS)</p>
    
    <form method="POST">
        <textarea name="comment" rows="4" cols="50" placeholder="Enter your comment..."></textarea><br>
        <button type="submit">Post Comment</button>
    </form>
    
    <h3>Try these XSS payloads:</h3>
    <div class="warning">
        <code>&lt;script&gt;alert('XSS')&lt;/script&gt;</code><br>
        <code>&lt;img src=x onerror=alert('Hacked')&gt;</code><br>
        <code>&lt;iframe src="javascript:alert(document.cookie)"&gt;</code>
    </div>
    
    <h3>Comments:</h3>
    <ul>
        {comments_html}
    </ul>
    '''
    
    return render_html('Comment - XSS Test', content)

@app.route('/debug')
def debug():
    # 🚨 VULNERABILITY: Information leakage
    debug_info = f"""
=== DEBUG INFORMATION ===

Session Data:
{dict(session)}

Request Information:
IP Address: {request.remote_addr}
User Agent: {request.user_agent}

App Secrets:
Secret Key: {app.secret_key}
Debug Mode: {app.debug}

Security Issues:
1. SQL Injection in /search
2. XSS in /comment  
3. Plain text passwords
4. Information leakage (this page!)
5. No input validation
6. No output encoding
"""
    
    content = f'''
    <h1>Debug Information</h1>
    <p>🚨 VULNERABILITY: Exposing sensitive information!</p>
    
    <pre>{debug_info}</pre>
    
    <div class="warning">
        <strong>Security Issue:</strong> This page should never be accessible in production!
        It exposes session data, app secrets, and internal information.
    </div>
    '''
    
    return render_html('Debug - Info Leak', content)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Another vulnerable endpoint - reflected XSS
@app.route('/echo')
def echo():
    text = request.args.get('text', '')
    
    content = f'''
    <h1>Echo Test</h1>
    <p>🚨 Reflected XSS Vulnerability</p>
    
    <form method="GET" action="/echo">
        <input type="text" name="text" value="{text}" placeholder="Enter text to echo...">
        <button type="submit">Echo</button>
    </form>
    
    {f'<h3>You said: {text}</h3>' if text else ''}
    
    <div class="warning">
        <strong>Try these XSS payloads:</strong><br>
        <code>&lt;script&gt;alert(1)&lt;/script&gt;</code><br>
        <code>&lt;img src=x onerror=alert(document.cookie)&gt;</code>
    </div>
    '''
    
    return render_html('Echo - XSS Test', content)

if __name__ == '__main__':
    print("=" * 60)
    print("🚨 INSECURE TEST APPLICATION STARTING")
    print("=" * 60)
    print("WARNING: This app has intentional security vulnerabilities!")
    print("DO NOT deploy on the internet or use in production!")
    print("=" * 60)
    print("\nAccess the app at: http://localhost:5000")
    print("\nTest these vulnerabilities:")
    print("1. SQL Injection: http://localhost:5000/search")
    print("2. XSS (Stored): http://localhost:5000/comment")
    print("3. XSS (Reflected): http://localhost:5000/echo?text=<script>alert(1)</script>")
    print("4. Weak Auth: http://localhost:5000/login")
    print("5. Info Leak: http://localhost:5000/debug")
    print("=" * 60)
    print("\nTest Credentials:")
    print("  admin / admin123")
    print("  user1 / password123")
    print("  test / test")
    print("=" * 60)
    
    # 🚨 Running with debug enabled (another vulnerability!)
    app.run(debug=True, host='0.0.0.0', port=5000)