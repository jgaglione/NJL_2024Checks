C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     ProjM(2,1)
C     
      SUBROUTINE FFS1_3(F1, F2, COUP, M3, W3,S3)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      REAL*8 M3
      REAL*8 P3(0:3)
      COMPLEX*16 S3(3)
      COMPLEX*16 TMP9
      REAL*8 W3
      COMPLEX*16 DENOM
      S3(1) = +F1(1)+F2(1)
      S3(2) = +F1(2)+F2(2)
      P3(0) = -DBLE(S3(1))
      P3(1) = -DBLE(S3(2))
      P3(2) = -DIMAG(S3(2))
      P3(3) = -DIMAG(S3(1))
      TMP9 = (F2(3)*F1(3)+F2(4)*F1(4))
      DENOM = COUP/(P3(0)**2-P3(1)**2-P3(2)**2-P3(3)**2 - M3 * (M3 -CI
     $ * W3))
      S3(3)= DENOM*CI * TMP9
      END


