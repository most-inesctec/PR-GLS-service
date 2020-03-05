function [Transform, C]=compute_prgls(X, Y)

    addpath('./CPD');
    mex cpd_P.c;
    mex cpd_Pappmex.c;
    mex cpd_Pcorrespondence.c;

    addpath('./SC');

    % Algorithm configurations
    opt.outliers = 0;
    opt.viz = 0;
    % Has no default value: confidence of featurs correspondence
    opt.t = 0.9;
    opt.sparse = 0;
    opt.nsc = 5;

    % Applying Point Set Registration
    % [Transform, C]=prgls_register(Y, X, opt);
    [Transform, C]=prgls_register(Y, X, opt);
end