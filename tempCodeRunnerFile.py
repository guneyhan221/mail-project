    if rememberme =="on":
                visiter_ip = request.remote_addr
                rmipf = open("rmip.txt",'a')
                rmipf.writelines(visiter_ip+"\n")
                rmipf.close()