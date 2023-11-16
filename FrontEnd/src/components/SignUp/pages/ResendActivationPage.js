import styles from './SignUpPage.module.css';
import DotDecorComponent from '../UI/dotDecor/DotDecor';
import { ResendActivationFormComponent } from '../components/signup/ResendActivationForm';

export function ResendActivationPage() {
  return (
    <div className={styles['sign-up']}>
      <div className={styles['sign-up__body']}>
        <DotDecorComponent position={'up-right'} />
        <div className={styles.container}>
          <ResendActivationFormComponent />
          <div className={styles['sign-in-line']}>
            <div className={styles['sign-in-line__text']}>
              Вже були на нашому сайті?
            </div>
            <a href="/login" className={styles['sign-in-line__link']}>
              Увійти
            </a>
          </div>
        </div>
        <DotDecorComponent position={'down-left'} />
      </div>
    </div>
  );
}
