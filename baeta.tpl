<!DOCTYPE html>
<html>
    <head>
        <title>Bæta Við</title>
    </head>
    <body>
        <h1>Bæta Við</h1>
        <form action="./buid" method="get" accept-charset="ISO-8859-1"><br>
            Eyða eða Bæta: <br>
            <select name="val">
                <option value="eyda">Eyða</option>
                <option value="baeta">Bæta</option>
                <option value="breyta">Breyta</option>
            </select><br>
            info: <br><input type="text" name="info" placeholder="Skráðu info hér" required><br>
            Breyta: <br><input type="text" name="id" placeholder="skrifaðu 0 eða 1(bara ef valið var Breyta fyrir ofan)"><br>
            <br><input type="submit" value="Skrá">
        </form>
    </body>
</html>
