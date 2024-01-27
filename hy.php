<!DOCTYPE html>
<html>
<head>
    <title>Read Text File</title>
    <style>
        body {
            font-family: "Courier New", monospace;
        }
    </style>
</head>
<body>
    <h1>Read Text File</h1>
    <pre id="content"></pre>

    <script>
        fetch('Hy2F.txt')
            .then(response => response.text())
            .then(data => {
                var preElement = document.getElementById("content");
                preElement.textContent = data;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    </script>
</body>
</html>
