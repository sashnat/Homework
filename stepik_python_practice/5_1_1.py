#print("Content-type: text/html")
#print()
print("<html>")
print(" <body>")
print("  <table>")
for i in range(1,11):
    print("   <tr>")
    for j in range(1,11):
        print("    <td>{0}</td>".format(i*j))
        #print("%4d" % (i*j), end='')
    print("   </tr>")
    #print()
print("  </table>")
print(" </body>")
print("</html>")
