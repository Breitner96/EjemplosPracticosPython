import numpy as np

# Ejemplo condicion inicial con el fin de realizar pruebas

arrayProduct=[{"Category":"tornilleria", "IdProduct":'123', "NameProduct":"Tuercas","SingleValue":2000, "BuyValue":2000*15, "MinStock":10, "MaxStock":20, "AvailableQuantity":15}]

def main():

    while True:


        print("Que Accion desea Realizar:\n Presione 1 Para Registrar un producto\n Presione 2 Para Remover un Producto del Inventario\n Presione 3 para mostrar productos Que esten por agostarse\n Presione 4 para ver el valor de venta de un Producto\n Presione 5 para ver los productos de una determinada Categoria\n Presione 6 si desea finalizar el proceso")

        try:

            x=int(input(':'))
            print("\n\n")

            if(x==1):

                category=input('Ingrese La categoria a la que pertenece, Tornilleria, Accesorios Bathrooms, Herramientas para Hogar: ')

                id_product=input('Indique el codigo de su producto: ')

                name_product=input('Indique el nombre de su producto: ')

                SingleValue=float(input('Indique el valor unitario de su producto: '))

            
                MinStock=int(input('Indique el Stock minimo de su producto: '))


                MaxStock=int(input('Indique el Stock maximo de su producto: '))

                AvailableQuantity=int(input('Indique la cantidad Disponible de su producto: '))

                BuyValue=float(SingleValue*AvailableQuantity)
                
                addProduct(category.lower(),id_product,name_product,SingleValue,BuyValue,MinStock,MaxStock,AvailableQuantity)
            
            elif(x==2):
                
                category=input('Ingrese La categoria del Producto a eliminar, Tornilleria, Accesorios Bathrooms, Herramientas para Hogar: ')

                id_product=input('Indique el codigo de su producto: ')

                RemoveProduct(category.lower(),id_product)

            elif(x==3):
                
                OutStockProduct()

            elif(x==4):
                
                category=input('Ingrese La categoria del Producto a visualizar, Tornilleria, Accesorios Bathrooms, Herramientas para Hogar: ')

                id_product=input('Indique el codigo de su producto: ')

                SellvalueProduct(category.lower(),id_product)

            elif(x==5):

                category=input('Ingrese La categoria que sea ver los Productos, Tornilleria, Accesorios Bathrooms, Herramientas para Hogar: ')

                ShowProducts(category.lower())




            elif(x==6):

                break


        except Exception:

            print("Digito la tecla Incorrecta")



    # OutStockProduct()    


def addProduct(category,id_product,name_product,SingleValue,BuyValue,minStock,maxStock,AvailableQuantity):
    
    arrayProduct.append({"Category":category, "IdProduct":id_product, "NameProduct":name_product,"SingleValue":SingleValue, "BuyValue":BuyValue, "MinStock":minStock, "MaxStock":maxStock, "AvailableQuantity":AvailableQuantity})

    print("Producto Registrado Correctamente\n\n")


def RemoveProduct(category,id_product):

    # result=[]

    try:

        newDict=[]
        finalDict=dict()

        for i in arrayProduct:
            
            for (key, value) in i.items():
                # Check if key is even then add pair to new dictionary
                if value == category:
                    newDict.append(i)
        
        for j in newDict:
            
            for (key, value) in j.items():
                # Check if key is even then add pair to new dictionary
                if value == id_product:
                    finalDict=j

        # print(finalDict)        

        if(finalDict):
        #    print (finalDict)

           finalDict=np.array(finalDict)

        #    print(finalDict)
           
           for x  in arrayProduct:
               if(np.array_equal(x,finalDict)):
                   arrayProduct.remove(x)
                   print("Producto Removido Correctamente")
                   print("Productos Restantes\n")

                   for j in arrayProduct:
                       print (j)
                       print("\n\n")

        else:
            print ("Categoria o codigo no encontrado\n\n\n\n")
        

    except:
        print("No se encontro ningun Resultado\n\n\n\n")

def OutStockProduct():

    # print("Productos")

    arrayOutStockProduct = []


    for i in arrayProduct:

        if(i['AvailableQuantity']<i['MinStock']):

            arrayOutStockProduct.append(i)

    if(arrayOutStockProduct):
        print("Productos fuera de Stock:\n")

        for x in arrayOutStockProduct:

            print(x)
            print("\n\n")

    else:
        print("Ningun Producto fuera de Stock\n\n")


def SellvalueProduct(category,id_product):

    try:

        newDict=[]
        finalDict=dict()

        for i in arrayProduct:
            
            for (key, value) in i.items():
                # Check if key is even then add pair to new dictionary
                if value == category:
                    newDict.append(i)
        
        for j in newDict:
            
            for (key, value) in j.items():
                # Check if key is even then add pair to new dictionary
                if value == id_product:
                    finalDict=j

        # print(finalDict)        

        if(finalDict):
        #    print (finalDict)

        #    finalDict=np.array(finalDict)

        #    print(finalDict)
           
           for x  in arrayProduct:
               if(np.array_equal(x,finalDict)):

                   print("\n\nProducto a Consultar\n")
                   
                   produc="Codigo del Producto: " + finalDict['IdProduct'] + "\nNombre del producto: " + finalDict['NameProduct'] + "\nCantidad disponible: " + str(finalDict['AvailableQuantity']) + "\nValor venta: " + str(finalDict['SingleValue'])
                   
                   print(produc+"\n\n")


        else:
            print ("Categoria o codigo no encontrado\n\n\n\n")
        

    except Exception as e:
        print("No se encontro ningun Resultado\n\n\n\n")
        print(e)

def ShowProducts(category):

    try:
        newDict=[]

        for i in arrayProduct:
            
            for (key, value) in i.items():
                # Check if key is even then add pair to new dictionary
                if value == category:
                    newDict.append(i)

        if(newDict):

            print("\n\nProductos de "+category+"\n")
            # print(newDict)
            for x in newDict:

                produc="Codigo del Producto: " + x['IdProduct'] + "\nNombre del producto: " + x['NameProduct'] + "\nCantidad disponible: " + str(x['AvailableQuantity']) + "\nValor venta: " + str(x['SingleValue'])
                
                print(produc)
                print("======================================")
                # print("Codigo del Producto: "+x['IdProduct'])
                # print("Nombre del producto: "+x['NameProduct'])
                # print("Cantidad disponible: "+x['AvailableQuantity'])
                # print("Valor venta: "+x['SingleValue'])
                print("\n\n")

                # print(x['AvailableQuantity'])
        else:
            print("\n\n")
            print("No se encontro ningun producto de la categoria "+category+"\n\n\n\n")    
        # print(type(result))
    except :
        print("No se encontro ningun Resultado")


if __name__ == '__main__':
    main()
