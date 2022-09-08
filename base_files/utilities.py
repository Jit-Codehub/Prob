import numeral
from numeral import int2roman
def roman_detail(res1):
        n1=int2roman(int(res1))
        f=[]
        for i in res1[::-1]:
                f.append(i)
        x1=[]
        l1=-1
        for i in f:
                l1+=1
                l2=str(i)+str(l1*"0")
                if int(l2)!=0:       
                        x1.append(l2)
        print(x1)
        x2=[]
        for i in x1:
                x2.append(int2roman(int(i)))
        print(x2)
        print(n1)
        x1=x1[::-1]
        x2=x2[::-1]
        a('<p>Arabic Number {} is expressed in the Roman Numeral Format as below</p><hr>'.format(res1))
        a('<table border="2"><tbody><th>Roman Numeral</th><th>=</th><th>Arabic Number</th>'.format(n1))
        for i,j in zip(x1,x2):
                a('<tr><td>{}</td><td>=</td><td style="text-align: right;">{}</td></tr>'.format(j,i))
        a('<tr><td>Total</td><td>=</td><td style="text-align: right;">{}</td></tr></tbody></table><br>'.format(res1))
        a('<p>We tried highlighting the place values of the given number 123 which you can combine and get the roman numeral accordingly.</p><br>')
        f=[]
        for i in res1[::-1]:
                f.append(i)
        x1=[]
        l1=-1
        for i in f:
                l1+=1
                l2=str(i)+str(l1*"0")
                if int(l2)!=0:       
                        x1.append(l2)
        print(x1,'iii')
        final=int2roman(int(res1))
        x2=[]
        for i in x1:
                x2.append(int2roman(int(i)))
        v=[]
        a=v.append
        if int(res1)<4000:
                a('<table border="2"><tr><td>Arabic<br>numerals</td>')
                for i in range(4-len(res1)):
                        a('<td class="big"></td>')
                for i in res1:
                        a('<td class="big">{}</td>'.format(i))
                a('</tr>')
                a('<tr><td>0</td><td id="r3-0"></td><td id="r2-0"></td><td id="r1-0"></td><td id="r0-0"></td></tr><tr><td>1</td><td id="r3-1">M</td><td id="r2-1">C</td><td id="r1-1">X</td><td id="r0-1">I</td></tr><tr><td>2</td><td id="r3-2">MM</td><td id="r2-2">CC</td><td id="r1-2">XX</td><td id="r0-2">II</td></tr><tr><td>3</td><td id="r3-3">MMM</td><td id="r2-3">CCC</td><td id="r1-3">XXX</td><td id="r0-3">III</td></tr><tr><td>4</td><td id="r3-4"></td><td id="r2-4">CD</td><td id="r1-4">XL</td><td id="r0-4">IV</td></tr><tr><td>5</td><td id="r3-5"></td><td id="r2-5">D</td><td id="r1-5">L</td><td id="r0-5">V</td></tr><tr><td>6</td><td id="r3-6"></td><td id="r2-6">DC</td><td id="r1-6">LX</td><td id="r0-6">VI</td></tr><tr><td>7</td><td id="r3-7"></td><td id="r2-7">DCC</td><td id="r1-7">LXX</td><td id="r0-7">VII</td></tr><tr><td>8</td><td id="r3-8"></td><td id="r2-8">DCCC</td><td id="r1-8">LXXX</td><td id="r0-8">VIII</td></tr><tr><td>9</td><td id="r3-9"></td><td id="r2-9">CM</td><td id="r1-9">XC</td><td id="r0-9">IX</td></tr>        </table>')
                b1=''.join(v)
                if int(res1)<4000:
                        u1=-1
                        for i in x1:
                                u1+=1
                                b1=b1.replace('id="r'+str(u1)+'-'+i[0]+'"','id="r'+str(u1)+'-'+i[0]+'" style="background-color: yellow;"')
                else:
                        pass
        return b1,final