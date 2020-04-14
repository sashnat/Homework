print("<html>")
print(" <body>")
print("  <table>")
for i in range(1,11):
    print("   <tr>")
    for j in range(1,11):
        b = i*j
        print ("    <td>","<a href=http://{0}.ru".format(b), ">{0}".format(b), "</a>", "</td>")
    print("   </tr>")

print("  </table>")
print(" </body>")
print("</html>")

