C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Metric(1,2)
C     
      SUBROUTINE VVSS1P1N_2(V1, S3, S4, COUP,V2)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 S3(*)
      COMPLEX*16 S4(*)
      COMPLEX*16 V1(*)
      COMPLEX*16 V2(6)
      V2(3)= COUP*(-CI )* V1(3)*S4(3)*S3(3)
      V2(4)= COUP*CI * V1(4)*S4(3)*S3(3)
      V2(5)= COUP*CI * V1(5)*S4(3)*S3(3)
      V2(6)= COUP*CI * V1(6)*S4(3)*S3(3)
      END


