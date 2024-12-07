<h1>Personal Blog</h1>

<p>A simple personal blog where you can write and publish articles. The blog is divided into two sections: a guest section for visitors to read articles and an admin section for managing articles.</p>

<h2>Features</h2>
<h3>Guest Section</h3>
<ul>
    <li><strong>Home Page:</strong> Displays a list of articles published on the blog.</li>
    <li><strong>Details Page:</strong> Shows the content of an article along with its details.</li>
</ul>

<h3>Admin Section</h3>
<ul>
    <li><strong>Dashboard:</strong> Lists all published articles with options to add, edit, or delete articles.</li>
    <li><strong>Add Article Page:</strong> A form to add new articles with fields for title and content.</li>
    <li><strong>Edit Article Page:</strong> A form to edit existing articles with fields for title and content.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Backend:</strong> Python, Django</li>
    <li><strong>Frontend:</strong> HTML, CSS, Django Templating Engine</li>
    <li><strong>Text Editor:</strong> CKEditor for rich text editing</li>
</ul>

<h2>Setup Instructions</h2>
<ol>
    <li>Clone this repository:</li>
    <pre><code>git clone https://github.com/Haknozer/Blogger.git </code></pre>
    <li>Navigate to the project directory:</li>
    <pre><code>cd Blogger</code></pre>
    <li>Install dependencies:</li>
    <pre><code>pip install django</code></pre>
    <pre><code>pip install django-ckeditor</code></pre>
    <pre><code>pip install python-slugify</code></pre>
    <li>Apply migrations:</li>
    <pre><code>python manage.py migrate</code></pre>
    <li>Create a superuser account for the admin:</li>
    <pre><code>python manage.py createsuperuser</code></pre>
    <li>Run the development server:</li>
    <pre><code>python manage.py runserver</code></pre>
    <li>Access the blog in your browser:</li>
    <ul>
        <li><strong>Guest Section:</strong> <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a></li>
        <li><strong>Admin Section:</strong> <a href="http://127.0.0.1:8000/admin/" target="_blank">http://127.0.0.1:8000/admin/</a></li>
    </ul>
</ol>


<h2>Future Enhancements</h2>
<ul>
    <li>Add article categories and filtering options.</li>
    <li>Integrate user comments for articles.</li>
    <li>Enhance authentication with more secure methods.</li>
    <li>Add pagination for articles on the home page.</li>
</ul>

https://roadmap.sh/projects/personal-blog 
https://roadmap.sh/projects/blogging-platform-api
