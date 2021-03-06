<!DOCTYPE html>
<html lang="${request.locale_name}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="pyramid web application">
    <link rel="shortcut icon" href="${request.static_url('ttt:static/pyramid-16x16.png')}">

    <title>rozetka parse form</title>

    <!-- Bootstrap core CSS -->
    <link href="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this scaffold -->
    <link href="${request.static_url('ttt:static/style.css')}" rel="stylesheet">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="//oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

  <div id="myform">
  <form class="form-inline" method="POST" action="/" >
      <div  class="form-group.col-md-12" id="lab">
          <label for="myselect"> Select category:</label>
            <select id="myselect" name="myselect">
                <option value="http://rozetka.com.ua/stabilizers/c144719/">Стабілізатори</option>
                <option value="http://rozetka.com.ua/servers/c125754/">Сервери</option>
                <option value="http://hard.rozetka.com.ua/monitors/c80089/">Монітори</option>
                <option value="http://rozetka.com.ua/bicycles/c83884/">Біциглі</option>
                <option value="http://rozetka.com.ua/telescopes/c89847/">Телескопи</option>
                <option value="http://rozetka.com.ua/rucksacks/c82445/">Рюкзаки</option>
            </select>
      </div>
  <div class="form-group">
    <label for="exampleInputName2"> Price from</label>
    <input type="text" class="form-control" id="exampleInputName2" name="pricefrom" placeholder="Price From">
  </div>
  <div class="form-group">
    <label for="exampleInputEmail2>"> Price to</label>
    <input type="text" class="form-control" id="exampleInputEmail2" name="priceto" placeholder="Price To">
  </div>
      <p>
  <button type="submit" class="btn btn-default" id="form-btn">submit</button>
      </p>
</form>
</div>

  <p>
  </p>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="//oss.maxcdn.com/libs/jquery/1.10.2/jquery.min.js"></script>
    <script src="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/js/bootstrap.min.js"></script>
  </body>
</html>



