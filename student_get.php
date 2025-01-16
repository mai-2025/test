
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Submit Student Request</title>
</head>
<body>
    <form action="http://localhost:8017/new_request_submit" method="POST">

        <input type="text" id="st_name" name="st_name" required>
        <label for="company_name">Company Name:</label>
        <input type="number" id="company_name" name="company_name">
        <input type="hidden" name="csrf_token" t-att-value="request.csrf_token()"/>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

