library("RSQLite")

# list.files(pattern="\\.pdResult$")

example_filename = "XLpeplib_Beveridge_QEx-HFX_DSS_R1.pdResult"

read_pdResult <- function(pdResult_filename){
  
  conn <- dbConnect(drv=RSQLite::SQLite(), dbname=pdResult_filename)
  
  target_psms <- dbGetQuery(conn=conn, statement="SELECT * FROM TargetPsms")
  decoy_psms <- dbGetQuery(conn=conn, statement="SELECT * FROM DecoyPsms")
  csms <- dbGetQuery(conn=conn, statement="SELECT * FROM CSMs")
  crosslinks <- dbGetQuery(conn=conn, statement="SELECT * FROM Crosslinks")
  
  dbDisconnect(conn)
  
  return(list(target_psms=target_psms, decoy_psms=decoy_psms, csms=csms, crosslinks=crosslinks))
}
