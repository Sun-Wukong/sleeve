# Deploy the script to the c:\scripts directory
Deploy 'Copy to scripts folder' {
  By Filesystem {
    FromSource '.\'
    To "c:\scripts\Sleeve"
    Tagged Prod
  }
}
