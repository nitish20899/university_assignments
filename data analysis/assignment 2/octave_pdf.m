pkg load statistics
pkg load optim
function octave_pdf
    X = -5:0.01:5;
    Y = normpdf(X);
    dY = @(num) normpdf(num);
    d0 = deriv(dY,X);
    d1 = @(X) deriv(dY,X);
    d2 = deriv(d1,X);
    plot(X, Y, "b*" , X, d0, "r*",  X, d2, "g*");
endfunction
octave_pdf()
