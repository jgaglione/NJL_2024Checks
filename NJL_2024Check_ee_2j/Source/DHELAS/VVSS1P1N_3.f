C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Metric(1,2)
C     
      SUBROUTINE VVSS1P1N_3(V1, V2, S4, COUP,S3)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 S3(3)
      COMPLEX*16 S4(*)
      COMPLEX*16 TMP5
      COMPLEX*16 V1(*)
      COMPLEX*16 V2(*)
      TMP5 = (V1(3)*V2(3)-V1(4)*V2(4)-V1(5)*V2(5)-V1(6)*V2(6))
      S3(3)= COUP*(-CI )* TMP5*S4(3)
      END

