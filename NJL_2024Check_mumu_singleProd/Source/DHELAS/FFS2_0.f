C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     ProjP(2,1)
C     
      SUBROUTINE FFS2_0(F1, F2, S3, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      COMPLEX*16 S3(*)
      COMPLEX*16 TMP2
      COMPLEX*16 VERTEX
      TMP2 = (F2(5)*F1(5)+F2(6)*F1(6))
      VERTEX = COUP*(-CI * TMP2*S3(3))
      END


