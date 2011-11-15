####

var1=int(raw_input ("Nhap vao ham mu muon tinh: "))
print 'ham_mu_' + str(var1)
var2= int(raw_input ("Nhap vao gia tri muon tinh:"))

def ham_mu(N):
    def calculate_exp(X):
        val = 1
        for i in range(N):
            val =val* X
        return val
    return calculate_exp
s=ham_mu(var1)
print 'ham_mu_' + str(var1) + '(' + str(var2) + ')'    +':  '+ str(s(var2))

raw_input("Press Enter to stop")
