<!DOCTYPE html>

<html lang="en">
<head>
    <!-- The jQuery library is a prerequisite for all jqSuite products -->
    <script type="text/ecmascript" src="/static/jsgrid5/js/jquery-1.11.0.min.js"></script>
    <!-- We support more than 40 localizations -->
    <script type="text/ecmascript" src="/static/jsgrid5/js/i18n/grid.locale-en.js"></script>
    <!-- This is the Javascript file of jqGrid -->   
    <script type="text/ecmascript" src="/static/jsgrid5/js/jquery.jqGrid.min.js"></script>
    <!-- This is the localization file of the grid controlling messages, labels, etc.
    <!-- A link to a jQuery UI ThemeRoller theme, more than 22 built-in and many more custom -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css"> 
    <!-- The link to the CSS that the grid needs -->
    <link rel="stylesheet" type="text/css" media="screen" href="/static/jsgrid5/css/ui.jqgrid-bootstrap.css" />
	<script>
		$.jgrid.defaults.width = 780;
        $.jgrid.defaults.styleUI = 'Bootstrap';
	</script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    <meta charset="utf-8" />
    <title>stabilisers</title>
</head>
<body>
<div style="margin-left:19%; margin-top: 25px">
    <table id="jqGrid"></table>
    <div id="jqGridPager"></div>
</div>
    <script type="text/javascript"> 
        $(document).ready(function () {
			

		$("#jqGrid").jqGrid({
		url: '/jres.json',
		datatype: "json",
		 colModel: [
			{ name: "name", label: "name", width: 690 },
            { name: "price", label: "price", width: 90, sorttype: 'integer' },

		],
		viewrecords: true, // show the current page, data rang and total records on the toolbar
		width: 780,
		height: 450,
		rowNum: 999,
		loadonce: true, // this is just for the demo
		pager: "#jqGridPager"
	});
});
 
   </script>

    
</body>
</html>