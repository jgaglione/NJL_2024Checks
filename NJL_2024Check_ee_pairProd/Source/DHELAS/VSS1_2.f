C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     P(1,2) - P(1,3)
C     
      SUBROUTINE VSS1_2(V1, S3, COUP, M2, W2,S2)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      REAL*8 M2
      REAL*8 P2(0:3)
      REAL*8 P3(0:3)
      COMPLEX*16 S2(3)
      COMPLEX*16 S3(*)
      COMPLEX*16 TMP2
      COMPLEX*16 TMP3
      COMPLEX*16 V1(*)
      REAL*8 W2
      COMPLEX*16 DENOM
      P3(0) = DBLE(S3(1))
      P3(1) = DBLE(S3(2))
      P3(2) = DIMAG(S3(2))
      P3(3) = DIMAG(S3(1))
      S2(1) = +V1(1)+S3(1)
      S2(2) = +V1(2)+S3(2)
      P2(0) = -DBLE(S2(1))
      P2(1) = -DBLE(S2(2))
      P2(2) = -DIMAG(S2(2))
      P2(3) = -DIMAG(S2(1))
      TMP2 = (P2(0)*V1(3)-P2(1)*V1(4)-P2(2)*V1(5)-P2(3)*V1(6))
      TMP3 = (V1(3)*P3(0)-V1(4)*P3(1)-V1(5)*P3(2)-V1(6)*P3(3))
      DENOM = COUP/(P2(0)**2-P2(1)**2-P2(2)**2-P2(3)**2 - M2 * (M2 -CI
     $ * W2))
      S2(3)= DENOM*S3(3)*(+CI*(TMP2)-CI*(TMP3))
      END


