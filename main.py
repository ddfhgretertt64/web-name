from flask import Flask, render_template_string, jsonify
from faker import Faker

app = Flask(__name__)
fake = Faker("en_US")

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>US Name Generator</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    padding:20px;
    background:#0f172a;
    font-family:Arial,sans-serif;
}

.card{
    width:100%;
    max-width:420px;
    background:#1e293b;
    border-radius:20px;
    padding:30px;
    text-align:center;
    box-shadow:0 10px 30px rgba(0,0,0,.35);
}

.title{
    color:#fff;
    font-size:24px;
    font-weight:700;
    margin-bottom:25px;
}

.name-box{
    background:#334155;
    color:#fff;
    font-size:28px;
    font-weight:700;
    padding:18px;
    border-radius:12px;
    word-break:break-word;
    margin-bottom:20px;
}

.copy-btn,
.change-btn{
    width:100%;
    border:none;
    border-radius:12px;
    padding:16px;
    font-size:18px;
    font-weight:600;
    cursor:pointer;
    color:white;
    transition:.2s;
}

.copy-btn{
    background:#3b82f6;
}

.change-btn{
    background:#16a34a;
    margin-top:10px;
}

.copy-btn:active,
.change-btn:active{
    transform:scale(.98);
}

.status{
    margin-top:12px;
    color:#22c55e;
    font-size:14px;
    height:18px;
}

@media (max-width:480px){

    .card{
        padding:24px;
    }

    .title{
        font-size:22px;
    }

    .name-box{
        font-size:24px;
        padding:16px;
    }

    .copy-btn,
    .change-btn{
        font-size:17px;
        padding:15px;
    }
}
</style>
</head>

<body>

<div class="card">

    <div class="title">
        US Name Generator
    </div>

    <div class="name-box" id="name">
        {{ name }}
    </div>

    <button class="copy-btn" id="copyBtn" onclick="copyName()">
        Copy Name
    </button>

    <button class="change-btn" onclick="changeName()">
        Change Name
    </button>

    <div class="status" id="status"></div>

</div>

<script>

async function copyName(){

    const name = document.getElementById("name").innerText;

    try{

        await navigator.clipboard.writeText(name);

        const btn = document.getElementById("copyBtn");
        const status = document.getElementById("status");

        btn.innerText = "Copied ✓";
        status.innerText = "Copied to clipboard";

        setTimeout(()=>{
            btn.innerText = "Copy Name";
            status.innerText = "";
        },1500);

    }catch(err){
        console.log(err);
    }
}

async function changeName(){

    try{

        const response = await fetch("/new-name");
        const data = await response.json();

        document.getElementById("name").innerText = data.name;

    }catch(err){
        console.log(err);
    }
}

</script>

</body>
</html>
"""

@app.route("/new-name")
def new_name():
    return jsonify({
        "name": fake.name()
    })

@app.route("/")
def home():
    return render_template_string(
        HTML,
        name=fake.name()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

