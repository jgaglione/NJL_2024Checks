C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     ProjP(2,1)
C     
      SUBROUTINE FFS2P1N_3(F1, F2, COUP,S3)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      COMPLEX*16 S3(3)
      COMPLEX*16 TMP3
      TMP3 = (F2(5)*F1(5)+F2(6)*F1(6))
      S3(3)= COUP*(-CI )* TMP3
      END


