pip install gegravity
 import pandas as pd
 import gme as gme
 import gegravity as ge
 gravity_data_location = r"C:\Users\singh\OneDrive\Desktop\IIT Kanpur\IITK 6th
 Semester\ECS\Herman-Trade\Real_Final_Data.csv"
 grav_data = pd.read_csv(gravity_data_location)
 grav_data
 gme_data = gme.EstimationData (grav_data,
 exp_var_name = "iso3_o_x",
 imp_var_name = "iso3_d_x",
 year_var_name = "year_x",
 trade_var_name = "exports") gme_model = gme.EstimationModel (gme_data, lhs_var
 ="Exports", rhs_var = ["contig_x", "comlang_off_x","lndist_x","international","asean","comlang
 _ethno_x","col45_x","aifta"], fixed_effects =[["iso3_o_x"], ["iso3_d_x"]]) gme_model.estimate()
 gme_model.results_dict["all"].summary()
 ge_model = ge.OneSectorGE ( gme_model , year = "2020", expend_var_name = "gdp_o_x",
 output_var_name = "gdp_d_x", reference_importer = "USA", sigma = 5)
 ge_model.build_baseline (omr_rescale =10)
 print(ge_model.baseline_mr) exp_data = ge_model.baseline_data.copy()
 #BRN exp_data.loc [( exp_data["iso3_d_x"]=="IND") & ( exp_data["iso3_o_x"]=="BRN") ,
 "asean"] = 1 exp_data.loc [( exp_data["iso3_d_x"]=="BRN") & ( exp_data["iso3_o_x"]=="IND") ,
 "asean"] = 1
 #KHMexp_data.loc [( exp_data["iso3_d_x"]=="IND") & ( exp_data["iso3_o_x"]=="KHM") ,
 "asean"] = 1 exp_data.loc [( exp_data["iso3_d_x"]=="KHM") & ( exp_data["iso3_o_x"]=="IND") ,
 "asean"] = 1
 #IDN exp_data.loc [( exp_data["iso3_d_x"]=="IND") & ( exp_data["iso3_o_x"]=="IDN") , "asean"]
 = 1exp_data.loc [(exp_data["iso3_d_x"]=="IDN") & (exp_data["iso3_o_x"]=="IND") ,"asean"] = 1
 #LAO exp_data.loc [( exp_data["iso3_d_x"]=="IND") & ( exp_data["iso3_o_x"]=="LAO") ,
 "asean"] = 1 exp_data.loc [( exp_data["iso3_d_x"]=="LAO") & ( exp_data["iso3_o_x"]=="IND") ,
 "asean"] = 1
 #MYS exp_data.loc [( exp_data["iso3_d_x"]=="IND") & ( exp_data["iso3_o_x"]=="MYS") ,
 "asean"] = 1 exp_data.loc [( exp_data["iso3_d_x"]=="MYS") & ( exp_data["iso3_o_x"]=="IND") ,
 "asean"] = 1
#MMRexp_data.loc [( exp_data["iso3_d_x"]=="IND") & ( exp_data["iso3_o_x"]=="MMR") ,
 "asean"] = 1 exp_data.loc [( exp_data["iso3_d_x"]=="MMR") & ( exp_data["iso3_o_x"]=="IND") ,
 "asean"] = 1
 #PHL exp_data.loc [( exp_data["iso3_d_x"]=="IND") & ( exp_data["iso3_o_x"]=="PHL") ,
 "asean"] = 1 exp_data.loc [( exp_data["iso3_d_x"]=="PHL") & ( exp_data["iso3_o_x"]=="IND") ,
 "asean"] = 1
 #SGP exp_data.loc [( exp_data["iso3_d_x"]=="IND") & ( exp_data["iso3_o_x"]=="SGP") ,
 "asean"] = 1 exp_data.loc [( exp_data["iso3_d_x"]=="SGP") & ( exp_data["iso3_o_x"]=="IND") ,
 "asean"] = 1
 #THA exp_data.loc [( exp_data["iso3_d_x"]=="IND") & ( exp_data["iso3_o_x"]=="THA") ,
 "asean"] = 1 exp_data.loc [( exp_data["iso3_d_x"]=="THA") & ( exp_data["iso3_o_x"]=="IND") ,
 "asean"] = 1
 #VNMexp_data.loc [( exp_data["iso3_d_x"]=="IND") & ( exp_data["iso3_o_x"]=="VNM") ,
 "asean"] = 1 exp_data.loc [( exp_data["iso3_d_x"]=="VNM") & ( exp_data["iso3_o_x"]=="IND") ,
 "asean"] = 1
 #Supply the updated data.
 ge_model.define_experiment(exp_data)
 ge_model.simulate()
 country_results = ge_model.country_results
 bilateral_results = ge_model.bilateral_trade_results
 ge_model.export_results (directory =r"C:\Users\singh\OneDrive\Desktop\IIT Kanpur\IITK 6th
 Semester\ECS\Another", name ="Results")