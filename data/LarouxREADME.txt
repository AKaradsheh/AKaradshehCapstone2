This supplemental material accompanies the manuscript: “Organizing and analyzing the activity data in NHANES” and contains the R code to reproduce all results presented in the manuscript (including all tables and figures associated with the analysis). When downloaded, the supplemental material will contain three directories:

code
figures
tables

Initially, all of these directories except for “code” will be empty. The figures and tables directories will be populated as the R code to run the analysis is execute.

There are a number of R scripts in the “code” directory. Users should only need to run the script “analysis_rnhanesdata_package.R”.

All other scripts are sourced by this script. The “analysis_rnhanesdata_package.R” script itself is heavily commented to walk users through each step of the analysis. In order to run the analysis script, users need only change a single line of code: at line 133 users will need to assign the “dir_supplemental” variable to be a character vector indicating the directory where the supplemental material folder is located. Once this has been done, everything else should run smoothly.

The analysis script with print a number of results to the console as well as save two figures (Figures 4 and 5 in the manuscript)
and the latex files needed to reproduce four tables (Tables 1, 4, 5, and 6). The names are:

Figures:
Figure 4: First 6 functional principal components - “functional_principal_components.jpeg”
Figure 5: Estimated functional coefficient plus illustration of the functional effect using two participants - “estimated_functional_coefficient.jpeg”
Tables:
Table 1: Included vs excluded population characteristics, unweights and survey weighted - “table1.tex”
Table 4: Cross-validated AUC for all single predictors - “table_auc_single_pred.tex”
Table 5: Cross-validated AUC for the full forward prediction procedure - “table_auc_forward_pred.tex”
Table 6: Survey weighted regression coefficients plus 95\% Wald confidence intervals for the odds of 5-year mortality - “table_final_regression.tex”