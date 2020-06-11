posicion=1
salto=""
while(posicion<=12):
    print("####################################################################################")#84
    print("JUMP RABBIT!", salto.upper())
    print("####################################################################################")#84
    print("AYUDA A SALTAR AL CONEJO AL OTRO EXTREMO")
    print("PARA JUGAR INGRESE(\"SALTAR DERECHA 1-2 HOPS\") MOVER DERECHA y (SALTAR IZQUIERDA 1-2 HOPS) para mover IZQUIERDA")

    conejo0=("  //\n"+
            " (·>\n"+
            " /rr\n"
            "*\))_ ")
    conejo1=("       //\n"+
        "      (·>\n"+
        "      /rr\n"
        "     *\))_ ")

    conejo2=("              //\n"+
        "             (·>\n"+
        "             /rr\n"
        "            *\))_ ")

    conejo3=("                     //\n"+
        "                    (·>\n"+
        "                    /rr\n"
        "                   *\))_ ")

    conejo4=("                            //\n"+
        "                           (·>\n"+
        "                           /rr\n"
        "                          *\))_ ")

    conejo5=("                                   //\n"+
        "                                  (·>\n"+
        "                                  /rr\n"
        "                                 *\))_ ")

    conejo6=("                                          //\n"+
        "                                         (·>\n"+
        "                                         /rr\n"
        "                                        *\))_ ")

    conejo7=("                                                 //\n"+
        "                                                (·>\n"+
        "                                                /rr\n"
        "                                               *\))_ ")

    conejo8=("                                                        //\n"+
        "                                                       (·>\n"+
        "                                                       /rr\n"
        "                                                      *\))_ ")

    conejo9=("                                                               //\n"+
        "                                                              (·>\n"+
        "                                                              /rr\n"
        "                                                             *\))_ ")

    conejo10=("                                                                      //\n"+
        "                                                                     (·>\n"+
        "                                                                     /rr\n"
        "                                                                    *\))_ ")

    conejo11=("                                                                             //\n"+
        "                                                                            (·>\n"+
        "                                                                            /rr\n"
        "                                                                           *\))_ ")

    conejo12=("                                                                                    //\n"+
        "                                                                                   (·>\n"+
        "                                                                                   /rr\n"
        "                                                                                  *\))_ ")


    if(posicion==0):
        print(conejo0)

    if(posicion==1):
        print(conejo1)

    if(posicion==2):
        print(conejo2)
    if(posicion==3):
        print(conejo3)

    if(posicion==4):
        print(conejo4)
    if(posicion==5):
        print(conejo5)

    if(posicion==6):
        print(conejo6)

    if(posicion==7):
        print(conejo7)

    if(posicion==8):
        print(conejo8)
    if(posicion==9):
        print(conejo9)
    if(posicion==10):
        print(conejo10)
    if(posicion==11):
        print(conejo11)
    if(posicion==12):
        print(conejo12)
    print("====================================================================================")#84
    print("0      1      2      3      4      5      6      7      8      9     10    11     12")
    print("====================================================================================")#84
    salto=input("INGRESE ACCION:")
    while(salto!="SALTAR DERECHA 1 HOPS" and salto!="SALTAR DERECHA 2 HOPS" and salto!="SALTAR IZQUIERDA 1 HOPS" and salto!="SALTAR IZQUIERDA 2 HOPS"):
        salto=input("INGRESE ACCION VALIDA: ")

    if(salto.upper()=="SALTAR DERECHA 1 HOPS"):
        posicion+=1

    if(salto.upper()=="SALTAR DERECHA 2 HOPS"):
        posicion+=2

    if(salto.upper()=="SALTAR IZQUIERDA 1 HOPS"):
        posicion-=1

    if(salto.upper()=="SALTAR IZQUIERDA 2 HOPS"):
        posicion-=2

    conejo2=("              //\n"+
    "             (·>\n"+
    "             /rr\n"
    "            *\))_ ")

    if(posicion<0):
        print("No HAY MAS JUMP, NO SEA IMBECIL")
        exit(-1)


print("USTED HA GANADO EL JUEGO")
