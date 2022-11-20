<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Recognition </title>
    <link rel="stylesheet" href="/static/css/style1.css">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <link rel="stylesheet" href="static/css/all.min.css">
</head>

<style>
    body{
     background-image: url('/static/assets/image3.jpeg');
     background-repeat: no-repeat;
     background-size: cover;
     height: 600px;
     
    }
    #title{
        font-family: 'Times New Roman', Times, serif;
    margin-top: 50px;
    overflow: hidden;
    text-align:center;
    font-weight: 900;
    
    }

    #rectangle{
     width:400px;
     height:170px;
     background-color: #fdfdfd;
     border-radius: 30px;
     position:absolute;
     top:50%;
     left:50%;
     transform:translate(-50%,-50%);
    }
    
    #ans{
  text-align: center;
  font-size: 35px;
  margin: 0 auto;
  padding: 3% 5%;
  padding-top: 15%;
  color: rgb(0, 0, 0);
    }

</style>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-transparent">
        <div class="container-fluid">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse navbar-nav-scroll justify-content-end" id="navbarScroll">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link text-dark" href="http://127.0.0.1:8000">Home</a>
              </li>
        
    <li class="nav-item">
        <a class="nav-link text-dark" href="http://127.0.0.1:8000/main">Recognize</a>
      </li>
    </li>
</ul>
</div>
</div>
</nav>
<div class="container">
    <h1  id="title" class="title text-dark"><b>Prediction</b></h1>
    </div>
<script src="/static/js/bootstrap.min.js"></script>
<script src="/static/js/jquery-3.6.1.js"></script>
    <div id="rectangle">
        <h1 id="ans" >Recognized Number : {{showcase}}</h1>
    </div>
</body>
</html>